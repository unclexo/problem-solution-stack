function tower(disc, a, b, c) {
  if (disc < 1) return;

  tower(disc - 1, a, c, b);
  console.log('Move disc ' + disc + ' from peg ' + a + ' to peg ' + c);
  tower(disc - 1, b, a, c);
}

tower(3, 'A', 'B', 'C');