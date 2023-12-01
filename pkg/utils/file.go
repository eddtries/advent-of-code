package utils

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func ReadFileToSlice(path string) (lines []string) {
	file, err := os.Open(path)
	if err != nil {
		log.Fatalln(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return
}

func StringToRuneSlice(str string) (chars []rune) {
	for _, rune := range str {
		chars = append(chars, rune)
	}

	return
}

func StringToCharsSlice(str string) (chars []string) {
	for _, char := range str {
		chars = append(chars, string(char))
	}

	return
}

func LineToInt(line string) (i int) {
	i, err := strconv.Atoi(line)
	if err != nil {
		fmt.Println(err)
	}

	return
}
