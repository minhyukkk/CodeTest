class Solution {
    int[] numbers;
    int target;
    int count = 0;
    // recursive 함수에서 사용하기 위해서 전역으로 선언

    public int solution(int[] numbers, int target) {
        this.numbers = numbers;
        this.target = target;
        // 전역으로 선언은 했지만 내가 가리키는 numbers와 target은 받아온 이 값이기 때문에 this 사용

        recursive(0, 0);
        return count;
    }

    public void recursive(int index, int answer) {
        if (index == numbers.length) {
            if (answer == target) {
                count++;
            }
            return; // index랑 똑같지만 target이랑 안똑같으면 return
        }

        recursive(index + 1, answer + numbers[index]);
        recursive(index + 1, answer - numbers[index]);
    }
}
