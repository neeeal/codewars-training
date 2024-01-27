const tester = require('./index');
const description = "Testing for fixed tests"
test(description, () => {
  expect(tester(2154959208)).toBe("128.114.17.104");
});
test(description, () => {
  expect(tester(0)).toBe("0.0.0.0");
});
test(description, () => {
  expect(tester(2149583361)).toBe("128.32.10.1");
});
test(description, () => {
  expect(tester(2 ** 32 - 1)).toBe("255.255.255.255");
});