package main

type node struct {
	level int64
	val int64
	left *node
	right *node
}

var root = *node{level: 0}

// A helper function for calculating max value.
func max[T](a, b T) T {
	if a > b {
		return a
	}

	return b
}

func treeProduct(root *node) (prod int64) {
	if root == nil {
		prod = 0
		return
	}

	// Using a queue to traverse each level.
	levelWatchlist := deque.Deque[*node]{root}
	prod = 1

	for Len(queue) > 0 {
		max := math.MinInt64 // Closest to -inf without using
		// float64.

		parent = levelWatchlist.PopBack()
		max = max(max, parent.val)

		// If current node has a left child, we add it to our
		// watchlist.
		if parent.left != nil {
			levelWatchlist.PushRight(parent.left)
		}
		// If current node has a right child, we add it to our
		// watchlist.
		if parent.right != nil {
			levelWatchlist.PushRight(parent.right)
		}

		prod *= max
	}

	return
}