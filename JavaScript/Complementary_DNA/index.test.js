const tester = require('./index');
const description = "Testing for fixed tests"
test(description, () => {
  expect(tester("AAAA")).toBe("TTTT");
});
test(description, () => {
  expect(tester("ATTGC")).toBe("TAACG");
});
test(description, () => {
  expect(tester("GTAT")).toBe("CATA");
});