const tester = require('./index');
const description = "Testing for fixed tests"
test(description, () => {
  expect(tester('man i need a taxi up to ubud')).toBe('taxi');
});
test(description, () => {
  expect(tester('what time are we climbing up the volcano')).toBe('volcano');
});
test(description, () => {
  expect(tester('take me to semynak')).toBe('semynak');
});
test(description, () => {
  expect(tester('aa b')).toBe('aa');
});
test(description, () => {
  expect(tester('aa b')).toBe('aa');
});
test(description, () => {
  expect(tester('aa b')).toBe('aa');
});
test(description, () => {
  expect(tester('aa b')).toBe('aa');
});