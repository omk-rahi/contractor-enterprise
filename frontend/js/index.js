import Swiper from "swiper";
import "swiper/css";

import "../scss/styles.scss";

import feather from "feather-icons";
import counterUp from "counterup2";

import * as bootstrap from "bootstrap";

feather.replace();

// COUNTER

const counterElements = document.querySelectorAll(".counter");

counterElements.forEach((el) => counterUp(el, { duration: 500 }));

// Hide alert

const alerts = Array.from(document.querySelectorAll(".custom-alert"));

setTimeout(() => {
  alerts.forEach((el) => {
    document.body.removeChild(el);
  });
}, 5000);

// PINCODE API

const getPincodeData = async (pincode) => {
  const res = await fetch(`https://api.postalpincode.in/pincode/${pincode}`);
  const data = await res.json();
  return data[0];
};

const pincodeInputField = document.querySelector("#id_pincode");

if (pincodeInputField) {
  pincodeInputField.addEventListener("change", async (e) => {
    const data = await getPincodeData(e.target.value);

    if (data.Status === "Error") {
      e.target.classList.add("is-invalid");
    } else {
      e.target.classList.remove("is-invalid");
    }

    if (data.Status === "Success") {
      const info = data.PostOffice[0];
      document.querySelector("#id_city").value = info.District;
      document.querySelector("#id_state").value = info.State;
    }
  });
}

// PRODUCT IMAGES

const productImages = Array.from(document.querySelectorAll(".product-images"));

if (productImages[0]) {
  productImages[0].parentElement.classList.add("active");
}

productImages.forEach((img) => {
  img.addEventListener("click", () => {
    const mainImg = document.querySelector("#product-image-main");
    mainImg.src = img.src;
    productImages.forEach((el) => el.parentElement.classList.remove("active"));
    img.parentElement.classList.add("active");
  });
});

// PRODUCT IMAGE SLIDER
const swiper = new Swiper(".swiper", {
  slidesPerView: 4,
  spaceBetween: 30,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  loop: false,
});

// RATING

const ratingOption = Array.from(document.querySelectorAll(".rating-option"));

ratingOption.forEach((el) => {
  el.addEventListener("click", (e) => {
    e.preventDefault();
    const ratingButton = document.querySelector(".rating-button span");

    ratingButton.innerHTML = e.target.closest(".rating-option").innerHTML;

    document.querySelector(".rating-input").value =
      e.target.closest(".rating-option").dataset.rating;
  });
});
