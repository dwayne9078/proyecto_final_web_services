class LandingPageScript {
  static handleNavBackground() {
    const nav = document.getElementsByTagName("nav")[0];
    window.addEventListener("scroll", () => {
        
      if (document.documentElement.scrollTop > 0) {
        nav.className = 'scrolled';
      } else {
        nav.className = '';
      }
    });
  }

  static handleColorScheme() {
    if (window.matchMedia("prefers-color-scheme: dark")) {
      console.log("TEMA OSCURO");
    }
  }
}


LandingPageScript.handleNavBackground();
LandingPageScript.handleColorScheme();