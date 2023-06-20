const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');

// Listen for changes to the prefers-color-scheme media query
prefersDark.addEventListener('change', (e) => checkToggle(e.matches));

if(prefersDark){
    document.querySelector('body').classList.add("dark")
}else{
    document.querySelector('body').classList.add('light')
}