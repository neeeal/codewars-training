const tester = require('./index');
const description = "Testing for fixed tests"
test(description, () => {
  expect(tester("")).toBe(false);
});
test(description, () => {
  expect(tester(" ".repeat(200))).toBe(false);
});
test(description, () => {
  expect(tester("Do We have A Hashtag")).toBe("#DoWeHaveAHashtag");
});
test(description, () => {
  expect(tester(("Codewars"))).toBe("#Codewars");
});
test(description, () => {
  expect(tester("Codewars Is Nice")).toBe("#CodewarsIsNice");
});
test(description, () => {
  expect(tester("Codewars is nice")).toBe("#CodewarsIsNice");
});
test(description, () => {
  expect(tester(("code" + " ".repeat(140) + "wars"))).toBe("#CodeWars");
});
test(description, () => {
  expect(tester("Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat")).toBe(false);
});
test(description, () => {
  expect(tester("a".repeat(139))).toBe("#A" + "a".repeat(138));
});
test(description, () => {
  expect(tester("a".repeat(140))).toBe(false);
});