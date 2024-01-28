const tester = require('./index');
const description = "Testing for fixed tests"
test(description, () => {
  expect(tester("hello")).toStrictEqual(["Hello", "hEllo", "heLlo", "helLo", "hellO"]);
});
test(description, () => {
  expect(tester("codewars")).toStrictEqual(["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]);
});
test(description, () => {
  expect(tester("")).toStrictEqual([]);
});
test(description, () => {
  expect(tester("two words")).toStrictEqual(["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]);
});
test(description, () => {
  expect(tester(" gap ")).toStrictEqual([" Gap ", " gAp ", " gaP "]);
});