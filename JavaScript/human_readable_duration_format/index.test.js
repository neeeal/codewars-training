const tester = require('./index');
const description = "Testing for fixed tests"
test(description, () => {
  expect(tester(1)).toBe("1 second");
});
test(description, () => {
  expect(tester(62)).toBe("1 minute and 2 seconds");
});
test(description, () => {
  expect(tester(120)).toBe("2 minutes");
});
test(description, () => {
  expect(tester(3600)).toBe("1 hour");
});
test(description, () => {
  expect(tester(3662)).toBe("1 hour, 1 minute and 2 seconds");
});
