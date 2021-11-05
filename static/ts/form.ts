const showPasswordByButton = () => {
  const inputPassword = document.querySelector(
    "input[type='password']"
  ) as HTMLInputElement;
  const button = document.querySelector(".container-checkbox")!;
  const showPasswordHandler = () => {
    const children = button.querySelector(".check-box")!;
    const valueIsClicked = children.classList.toggle("check-box-open");
    if (valueIsClicked) {
      inputPassword.setAttribute("type", "text");
    } else {
      inputPassword.setAttribute("type", "password");
    }
  };
  button.addEventListener("click", showPasswordHandler);
};

showPasswordByButton();

// const validationInput = (
//   input: Element,
//   lengthCondtion: number,
//   functionCondition: (value: string) => boolean
// ) => {
//   let isValid = true;
//   let inputIsValid = true;
//   input.addEventListener("input", (event: Event) => {
//     const target = event.target as HTMLInputElement;
//     const valueInput = target.value;
//     if (valueInput.trim().length <= lengthCondtion && functionCondition(valueInput)) {
//       isValid = false;
//     } else {
//       isValid = true;
//     }
//     inputIsValid = isValid && isTouched
//   });
//   let isTouched = false;
//   const blurHandlerEvent = () => {
//     isTouched = true;
//   };
//   input.addEventListener("blur", blurHandlerEvent);

//   return {
//     isValid,
//     isTouched,
//     inputIsValid
//   };
// };

// interface validateInput {
//     isValid: boolean,
//     isTouched: boolean,
//     inputIsValid: boolean
// }

// const checkValidateInput = () => {
//     const emailInput = document.querySelector('#email')!;
//     const validateEmail: validateInput = validationInput(emailInput, 0, value => value.includes('@'));
//     console.log(validateEmail.inputIsValid);
// }
// checkValidateInput();