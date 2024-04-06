import { DiceRoll } from "./dice_roll.js";
export function rollDice() {
    const GAME = new DiceRoll();
    GAME.play();
}

rollDice();
