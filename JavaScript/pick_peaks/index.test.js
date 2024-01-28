const tester = require('./index');
const description = "Testing for fixed tests"
test(description, () => {
  expect(tester([1,2,3,6,4,1,2,3,2,1])).toStrictEqual({pos:[3,7], peaks:[6,3]});
});
test(description, () => {
  expect(tester([3,2,3,6,4,1,2,3,2,1,2,3])).toStrictEqual({pos:[3,7], peaks:[6,3]});
});
test(description, () => {
  expect(tester([3,2,3,6,4,1,2,3,2,1,2,2,2,1])).toStrictEqual({pos:[3,7,10], peaks:[6,3,2]});
});
test(description, () => {
  expect(tester([2,1,3,1,2,2,2,2,1])).toStrictEqual({pos:[2,4], peaks:[3,2]});
});
test(description, () => {
  expect(tester([2,1,3,1,2,2,2,2])).toStrictEqual({pos:[2], peaks:[3]});
});
test(description, () => {
  expect(tester([2,1,3,2,2,2,2,5,6])).toStrictEqual({pos:[2], peaks:[3]});
});
test(description, () => {
  expect(tester([2,1,3,2,2,2,2,1])).toStrictEqual({pos:[2], peaks:[3]});
});
test(description, () => {
  expect(tester([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3])).toStrictEqual({pos:[2,7,14,20], peaks:[5,6,5,5]});
});
test(description, () => {
  expect(tester([])).toStrictEqual({pos:[],peaks:[]});
});
test(description, () => {
  expect(tester([1,1,1,1])).toStrictEqual({pos:[],peaks:[]});
});
