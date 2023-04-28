// select all the dom elements needed

const tabs = document.querySelectorAll(".operations__tab");
const tabsContainer = document.querySelector(".operations__tab-container");
const tabsContent = document.querySelectorAll(".operations__content");

tabsContainer.addEventListener("click", function (e) {
  const clicked = e.target.closest(".operations__tab");
  //console.log(clicked);
  if (!clicked) return;

  tabsContent.forEach((content) =>
    content.classList.remove("operations__content--active")
  );
  tabs.forEach((tab) => tab.classList.remove("operations__tab--active"));
  //console.log(clicked.dataset.tab);
  //activate content area
  document
    .querySelector(`.operations__content--${clicked.dataset.tab}`)
    .classList.add("operations__content--active");
  document
    .querySelector(`.operations__tab--${clicked.dataset.tab}`)
    .classList.add("operations__tab--active");
});
