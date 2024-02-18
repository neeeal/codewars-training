const [zero, one, two, three, four, five, six, seven, eight, nine, plus, minus, times, dividedBy] = require('./index');
const description = "Testing for fixed tests"
test(description, () => {
  expect(seven(times(five()))).toBe(35);
});
test(description, () => {
  expect(four(plus(nine()))).toBe(13);
});
test(description, () => {
  expect(eight(minus(three()))).toBe(5);
});
test(description, () => {
  expect(six(dividedBy(two()))).toBe(3);
});
