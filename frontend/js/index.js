import "../scss/styles.scss";

import feather from "feather-icons";
import counterUp from "counterup2";

import * as bootstrap from "bootstrap";

feather.replace();

// COUNTER

const counterElements = document.querySelectorAll(".counter");

counterElements.forEach((el) => counterUp(el, { duration: 500 }));
