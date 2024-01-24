const tester = require('./index');
const description = "Testing for fixed tests"
test(description, () => {
  expect(tester("http://google.com")).toBe("google");
});
test(description, () => {
  expect(tester("http://google.co.jp")).toBe("google");
});
test(description, () => {
  expect(tester("www.xakep.ru")).toBe("xakep");
});
test(description, () => {
  expect(tester("https://youtube.com")).toBe("youtube");
});
