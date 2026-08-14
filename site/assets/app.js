const languageKey = "repocover-language";

for (const link of document.querySelectorAll("[data-language-link]")) {
  link.addEventListener("click", () => {
    localStorage.setItem(languageKey, link.dataset.languageLink);
  });
}

for (const button of document.querySelectorAll("[data-copy]")) {
  button.dataset.copyReady = "true";
  button.addEventListener("click", async () => {
    const selector = button.dataset.copy;
    const target = document.querySelector(selector);
    if (!target) return;

    const original = button.textContent;
    const value = target.textContent.trim();
    let copied = false;
    try {
      await navigator.clipboard.writeText(value);
      copied = true;
    } catch {
      const fallback = document.createElement("textarea");
      fallback.value = value;
      fallback.setAttribute("readonly", "");
      fallback.style.position = "fixed";
      fallback.style.opacity = "0";
      document.body.append(fallback);
      fallback.select();
      copied = document.execCommand("copy");
      fallback.remove();
    }

    if (copied) {
      button.textContent = button.dataset.copied || "Copied";
      window.setTimeout(() => {
        button.textContent = original;
      }, 1800);
    } else {
      button.textContent = document.documentElement.lang === "zh-CN" ? "请手动复制" : "Select text";
      target.focus?.();
    }
  });
}

for (const year of document.querySelectorAll("[data-current-year]")) {
  year.textContent = new Date().getFullYear();
}
