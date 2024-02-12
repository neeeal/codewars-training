const tester = require('./index');
const description = "Testing for fixed tests"
test(description, () => {
  expect(tester(0,   0,   0)).toBe("000000");
});
test(description, () => {
  expect(tester(0,   0, -20)).toBe("000000");
});
test(description, () => {
  expect(tester(300, 255, 255)).toBe("FFFFFF");
});
test(description, () => {
  expect(tester(173, 255,  47)).toBe("ADFF2F");
});
