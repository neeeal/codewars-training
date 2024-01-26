const tester = require('./index');
const description = "Testing for fixed tests"
test(description, () => {
  expect(tester(12)).toBe('10 + 2');
});
test(description, () => {
  expect(tester(42)).toBe('40 + 2');
});
test(description, () => {
  expect(tester(70304)).toBe('70000 + 300 + 4');
});