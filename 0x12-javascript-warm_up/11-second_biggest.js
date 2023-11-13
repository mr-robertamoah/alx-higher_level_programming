#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let i;
  const nums = [];
  for (i = 2; i < process.argv.length; i++) {
    nums.push(parseInt(process.argv[i]));
  }
  let maxn = nums[0];
  for (let i = 0; i < nums.length; i++) {
    if (maxn < nums[i]) {
      maxn = nums[i];
    }
  }
  let secondn = nums[0];
  for (i = 0; i < nums.length; i++) {
    if ((secondn === maxn || secondn < nums[i]) && nums[i] !== maxn) {
      secondn = nums[i];
    }
  }
  console.log(secondn);
}
