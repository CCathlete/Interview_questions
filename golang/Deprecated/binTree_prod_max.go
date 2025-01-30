//go:build ignore

// -------------------- Description ---------------------------
/*
Given a binary tree, return the product of the largest value in each level of the tree.

Example solution: 1- * 4 * 12 * 24 * 12 = 138,240
*/

// ---------------- Ask the interviewer ----------------------
/*
1. How is a tree represented? It is a node struct (val, left, right).

2. Since we are calcuating products, can this overflow? (bottleneck in garbage collection)
--> Usually not a consideration in an interview but it's good to ask.

3. How should I treat a null tree (root is null)? Return nil or 0?
*/

// ----------------------- Method ----------------------------
// ---------- Explain and verify that that's ok --------------
/*
BFS (horizontal scan) with a queue to keep track of the largest
value of each level. At the end of each level we multiply the value with a running product.
*/
package main

import "fmt"

type node struct {
	level int64
	val   int64
	left  *node
	right *node
}

var root = &node{level: 0}
var maxVals []int64
var prod = int64(1)

func bfs(node *node) (max int64) {
	var maxL, maxR int64

	if node == root {
		maxVals = append(maxVals, node.val)
		prod *= node.val
	}

	if node.right != nil {
		maxR = TreeProduct(node.right)
	}
	if node.left != nil {
		maxL = TreeProduct(node.left)
	}
	if node.right == nil && node.left == nil {
		// We're on a leaf.
		return node.val
	}

	// If we're here, we're not on a leaf.
	if maxL >= maxR {
		max = maxL
	} else {
		max = maxR
	}
	maxVals = append(maxVals, max)
	prod *= max

	return
}

func TreeProduct(root *node) (product int64) {
	bfs(root)
	product = prod

	return
}

func printEquation() {
	eq := fmt.Sprintf("%d * ", maxVals[0])

	for val := range maxVals[1:] {
		eq = fmt.Sprintf("%s * %d", eq, val)
	}

	eq = fmt.Sprintf("%s = %d", eq, prod)

	fmt.Println(eq)
}

func main() {
	root.val = 1
	root.left = &node{level: 1, val: 4}
	root.right = &node{level: 1, val: 12}
	root.left.left = &node{level: 2, val: 24}
	root.left.right = &node{level: 2, val: 12}

	TreeProduct(root)
	printEquation()
}
