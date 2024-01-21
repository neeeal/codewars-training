const tester = require('./index');
const description = "Testing for fixed tests"
test(description, () => {
  expect(tester([[10,0],[3,5],[5,8]])).toBe(5);
});
test(description, () => {
  expect(tester([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])).toBe(17);
});
test(description, () => {
  expect(tester([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])).toBe(21);
});
test(description, () => {
  expect(tester([[0,0]])).toBe(0);
});