import defaultTheme from 'tailwindcss/defaultTheme'

/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			fontFamily: {
				sans: ['Inter Variable', ...defaultTheme.fontFamily.sans],
				serif: ['Merriweather', ...defaultTheme.fontFamily.serif]
			},
			colors: {
				"accent": "rgb(var(--accent))",
				"primary": "rgb(var(--primary))",
				"primary-light": "rgb(var(--primary-light))",
				"accent-light": "rgb(var(--accent-light))",
				"secondary": "rgb(var(--secondary))",
			}
		},
	},
	plugins: [],
}