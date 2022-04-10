const {sum, subtraction} = require('./operations');

test('2 + 3 expected to be 5', () => {
  expect(sum(2, 3)).toBe(5);
});

test('15 - 10 expected to 5', () => {
  expect(subtraction(15, 10)).toBe(5);
});
