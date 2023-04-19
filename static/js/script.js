"use strict";

const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay");
const btnCloseModal = document.querySelector(".btn--close-modal");
const btnsOpenModal = document.querySelectorAll(".btn--show-modal");
const btnScrollTo = document.querySelector(".btn--scroll-to");
const section1 = document.querySelector("#section--1");
const tabs = document.querySelectorAll(".operations__tab");
const tabsContainer = document.querySelector(".operations__tab-container");
const tabsContent = document.querySelectorAll(".operations__content");
const nav = document.querySelector(".nav");

///////////////////////////////////////
//Modal window

const openModal = function (e) {
  // Prevent the behavior of when clicking a link, the page would scroll to the top
  e.preventDefault();
  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");
};

// implement scrolling to next section when clicking on "learn more"
btnScrollTo.addEventListener("click", function (e) {
  const s1coords = section1.getBoundingClientRect();
  console.log(s1coords);

  //console.log(e.target.getBoundingClientRect());

  // get the distance between the current position(the edge of the page) and the view port (this is a relative value)
  console.log("Current scroll (X/Y)", window.pageXOffset, window.pageYOffset);
  console.log(
    "height/width viewport",
    document.documentElement.clientHeight,
    document.documentElement.clientWidth
  );

  // Call the scrollIntoView method so that the element will be visible to the user
  section1.scrollIntoView({ behavior: "smooth" }); // only supports modern browsers
});

// Tabbed component

tabsContainer.addEventListener("click", function (e) {
  // gets the button elements
  const clicked = e.target.closest(".operations__tab");
  // console.log(clicked);
  // Guard clause
  if (!clicked) return; // if there is no clicked element (which returns null), it will then terminates the event listener immediately

  // remove the operations__tab--active class from all the tabs and then adds it on the clicked element
  tabs.forEach((t) => t.classList.remove("operations__tab--active"));
  clicked.classList.add("operations__tab--active");

  tabsContent.forEach((c) => c.classList.remove("operations__content--active"));
  // console.log(clicked.dataset.tab);
  // Activate content area
  document
    .querySelector(`.operations__content--${clicked.dataset.tab}`)
    .classList.add("operations__content--active");
});

// Menu fade animation

const handleHover = function (e) {
  if (e.target.classList.contains("nav__link")) {
    const link = e.target;
    const siblings = link.closest(".nav").querySelectorAll(".nav__link");
    const logo = link.closest(".nav").querySelector("img");

    siblings.forEach((el) => {
      if (el !== link) el.style.opacity = this;
    });
    logo.style.opacity = this;
    // console.log(this, e.currentTarget);
  }
};
// Passing 'argument' into handler
// the bind method creates a copy of the current function it is called on and then set its this key word as the value we passed in
nav.addEventListener("mouseover", handleHover.bind(0.5));

nav.addEventListener("mouseout", handleHover.bind(1));

// Sticky navigation

const header = document.querySelector(".header");
const navHeight = nav.getBoundingClientRect().height;

const stickyNav = function (entries) {
  const [entry] = entries;
  // console.log(entries);
  // when intersection is false (intersection ratio = 0) then add the class sticky
  if (!entry.isIntersecting) nav.classList.add("sticky");
  else nav.classList.remove("sticky");
};

const headerObserver = new IntersectionObserver(stickyNav, {
  root: null,
  threshold: 0,
  rootMargin: `-${navHeight}px`,
});

// the intersection observer is now observing the header
headerObserver.observe(header);

//// Reveal sections
const allSections = document.querySelectorAll(".section");

const revealSection = function (entries, observer) {
  const [entry] = entries;
  // console.log(entries);

  if (!entry.isIntersecting) return;
  entry.target.classList.remove("section--hidden");

  // keeps all the sections on display
  observer.unobserve(entry.target);
};

const sectionObserver = new IntersectionObserver(revealSection, {
  root: null,
  // reveal the section when it's 15% visible
  threshold: 0.15,
});

allSections.forEach(function (section) {
  section.classList.add("section--hidden");
  sectionObserver.observe(section);
});

//// lazy loading images

const imgTargets = document.querySelectorAll("img[data-src]");
// console.log(imgTargets)

const loadImg = function (entries, observer) {
  const [entry] = entries;
  // console.log(entry);
  if (!entry.isIntersecting) return;

  // Replace src with data-src
  entry.target.src = entry.target.dataset.src;

  // Remove the lazy-img class that added the filter (if we remove the class directly then if the user has a slow network or phone, it won't be very user friendly)
  entry.target.addEventListener("load", function () {
    // when the images finished loading remove the class
    entry.target.classList.remove("lazy-img");
  });

  observer.unobserve(entry.target);
};

const imgObserver = new IntersectionObserver(loadImg, {
  root: null,
  threshold: 0,
  // load the image before the viewport reaches the images
  rootMargin: "200px",
});

imgTargets.forEach((img) => imgObserver.observe(img));

///////////////////////////////////////
// Slider
const slider = function () {
  const slides = document.querySelectorAll(".slide");
  const btnLeft = document.querySelector(".slider__btn--left");
  const btnRight = document.querySelector(".slider__btn--right");
  const dotContainer = document.querySelector(".dots");

  // const slider = document.querySelector('.slider');
  // slider.style.overflow = 'visible';
  let curSlide = 0;
  const maxSlide = slides.length;

  slides.forEach(
    (slide, index) => (slide.style.transform = `translateX(${100 * index}%)`)
  );
  // 0%, 100%, 200%, 300%

  const createDots = function () {
    slides.forEach(function (_, i) {
      dotContainer.insertAdjacentHTML(
        "beforeend",
        `<button class="dots__dot" data-slide="${i}"></button>`
      );
    });
  };

  const activateDot = function (slide) {
    document
      .querySelectorAll(".dots__dot")
      .forEach((dot) => dot.classList.remove("dots__dot--active"));

    document
      .querySelector(`.dots__dot[data-slide="${slide}"]`)
      .classList.add("dots__dot--active");
  };

  const goToSlide = function (slide) {
    slides.forEach(
      (s, i) => (s.style.transform = `translateX(${100 * (i - slide)}%)`)
    );
  };

  // Go to the next slide
  const nextSlide = function () {
    if (curSlide === maxSlide - 1) {
      curSlide = 0; // return to the first slide
    } else {
      curSlide++;
    }

    slides.forEach(
      (slide, index) =>
        (slide.style.transform = `translateX(${100 * (index - curSlide)}%)`)
    );
    // curSlide = 1, -100% (index = 0), 0% (index = 1), 100%(index = 2), 200%(index = 3)
    activateDot(curSlide);
  };

  // Go to the previous slide
  const previousSlide = function () {
    if (curSlide === 0) {
      curSlide = maxSlide - 1; // go to the last slide
    } else {
      curSlide--;
    }
    slides.forEach(
      (slide, index) =>
        (slide.style.transform = `translateX(${100 * (index - curSlide)}%)`)
    );
    activateDot(curSlide);
  };

  const init = function () {
    goToSlide(0);
    createDots();

    activateDot(0);
  };
  init();

  btnRight.addEventListener("click", nextSlide);
  btnLeft.addEventListener("click", previousSlide);

  document.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") previousSlide();
    else if (e.key === "ArrowRight") nextSlide();
  });
};
slider();
