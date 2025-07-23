/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", //template er vitore nested ja ase sobv search kore tailwind .....also it searches at root lvel
     "./**templates/**/*.html"  //app lvl ee search kore...
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

