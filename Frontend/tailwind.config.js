/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        "background-page": "#F0EAD6",
        "text-secondary": "#173044",
        "primary-color": "#013220",
        "text-primary": "#F1E4EB",
        "btn-info": "#4A1942",
        "btn-success": "#469B9C",
        "btn-warning": "#B87333",
        "btn-delete": "#B0413E",
      },
      lineClamp: {
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        20: "20",
      },
    },
  },
  plugins: [],
};
