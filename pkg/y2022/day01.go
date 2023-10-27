package y2022

import (
	"fmt"
	"sort"
	"strconv"

	"github.com/eddtries/advent-of-code/pkg/utils"
)

func Day01() {
	elf := 0
	var elves []int

	lines := utils.ReadFileToSlice("./pkg/y2022/data/day01.data")
	for _, line := range lines {
		if line == "" {
			elves = append(elves, elf)
			elf = 0
		} else {
			i, err := strconv.Atoi(line)
			if err != nil {
				fmt.Println(err)
			}
			elf += i
		}
	}

	sort.Ints(elves)

	println("Part 1: " + fmt.Sprint(elves[len(elves)-1]))
	println("Part 2: " + fmt.Sprint(elves[len(elves)-1]+elves[len(elves)-2]+elves[len(elves)-3]))
}
