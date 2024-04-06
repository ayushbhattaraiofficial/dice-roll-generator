export class DiceRoll {
    constructor() {
        this.sides = prompt("How many sides per die?");
        this.dice = prompt("Enter the number of dice to throw");
    }

    roll() {
        return Math.floor(Math.random() * this.sides) + 1;
    }

    play() {
        var sum = 0;
        var result_string = "";
        while (this.dice > 0) {
            var result = this.roll();
            sum += result;
            result_string += `${String(result)}, `;
            this.dice -= 1;
        }
        result_string += `sum is ${String(sum)}`;
        alert(`${result_string}`);
    }
}
