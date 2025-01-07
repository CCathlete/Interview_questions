package main

import (
	"fmt"
	"math"

	"github.com/gammazero/deque"
)

type node struct {
	level int64
	val   int64
	left  *node
	right *node
}

var root = &node{level: 0}

// A helper function for calculating max value.
func Max[T int | int64 | float64](a, b T) T {
	if a > b {
		return a
	}

	return b
}

var eq string

func treeProduct(root *node) (prod int64) {
	if root == nil {
		prod = 0
		return
	}

	// Using a queue to traverse each level.
	levelWatchlist := &deque.Deque[*node]{}
	levelWatchlist.PushFront(root)
	prod = 1

	for levelWatchlist.Len() > 0 {
		max := int64(math.MinInt64) // Closest to -inf without using float64.

		parent := levelWatchlist.PopBack()
		max = Max(max, parent.val)
		eq += fmt.Sprintf("%d * ", max)

		// If current node has a left child, we add it to our
		// watchlist.
		if parent.left != nil {
			levelWatchlist.PushFront(parent.left)
		}
		// If current node has a right child, we add it to our
		// watchlist.
		if parent.right != nil {
			levelWatchlist.PushFront(parent.right)
		}

		prod *= max
	}

	eq = fmt.Sprintf("%s =", eq)
	return
}

func main() {
	root.val = 10
	root.left = &node{level: 1, val: 4}
	root.right = &node{level: 1, val: 12}
	root.left.left = &node{level: 2, val: 24}
	root.left.right = &node{level: 2, val: 12}

	fmt.Println(eq, treeProduct(root))
}
