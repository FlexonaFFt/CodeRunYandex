package main

import (
	"fmt"
)

func largestSquare(n, m int, grid [][]int) {
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, m)
	}

	maxSide := 0
	maxI := 0
	maxJ := 0

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if grid[i][j] == 1 {
				if i == 0 || j == 0 {
					dp[i][j] = 1
				} else {
					dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
				}

				if dp[i][j] > maxSide {
					maxSide = dp[i][j]
					maxI = i
					maxJ = j
				} else if dp[i][j] == maxSide {
					if j > maxJ || (j == maxJ && i > maxI) {
						maxI = i
						maxJ = j
					}
				}
			}
		}
	}

	// координаты верхнего левого угла квадрата
	topLeftI := maxI - maxSide + 1
	topLeftJ := maxJ - maxSide + 1

	// добавляем единицу к координатам, чтобы привести их к формату ввода-вывода (1-индексация)
	fmt.Println(maxSide)
	fmt.Println(topLeftI+1, topLeftJ+1)
}

func min(a, b, c int) int {
	if a < b {
		if a < c {
			return a
		}
		return c
	}
	if b < c {
		return b
	}
	return c
}

func main() {
	var n, m int
	fmt.Scan(&n, &m)

	grid := make([][]int, n)
	for i := range grid {
		grid[i] = make([]int, m)
		for j := 0; j < m; j++ {
			fmt.Scan(&grid[i][j])
		}
	}

	largestSquare(n, m, grid)
}
