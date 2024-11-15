#!/usr/bin/nodejs

const galeShapleyMenPropose = (m, w) => {
    console.log("Men Propose");
    let free_men = []

   for (const [key, value] of Object.entries(m)){
    console.log(`${key}: ${value}`);
   }

   Object.entries(m).forEach(([k, v]) => {
    console.log(k, v)
   })
   Object.keys(m).forEach(k => {
     free_men.push(k)
   })

   Object.values(m).forEach(v => {
    console.log(v)
   })

   const g = [2, 44, 55, 223, 77, 99];
   for (const i of g) {
    console.log(i);
   }
   for (let i = 0; i < g.length; i++)
   {
    console.log(g[i])
   }

   console.log(free_men)

   let result = Object.entries(w).reduce((acc, [key, value]) => {
    acc[key] = 'none';  

}, {});
    console.log(result)
    console.log("==========================")
}
const galeShapleyWomenPropose = (w, m) => {
    console.log("women propose");
}

// galeShapleyMenPropose(men_preferences, women_preferences)
// galeShapleyWomenPropose(men_preferences, women_preferences)
// input: 2d Array. or sigle array   [[1, 'none'], [2, 'none'], [3, 'none']]

const free_men = Object.fromEntries(
    Object.keys(men_preferences).map(man => [man, 0])
);

console.log(free_men);
