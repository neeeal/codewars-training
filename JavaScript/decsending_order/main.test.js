const tester = require('./main');
const description = "Testing for fixed tests"
test(description, () => {
  expect(tester(0)).toBe(0);
});
test(description, () => {
  expect(tester(1)).toBe(1);
});
test(description, () => {
  expect(tester(111)).toBe(111);
});
test(description, () => {
  expect(tester(15)).toBe(51);
});
test(description, () => {
  expect(tester(1021)).toBe(2110);
});
test(description, () => {
  expect(tester(123456789)).toBe(987654321);
});