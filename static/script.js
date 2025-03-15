(function()  {
  const languageChoiceElement = document.querySelector("#languageChoice");
  const codeSnippet = document.querySelector("#code-script");
  const runCode = document.querySelector("#run-code");

  languageChoiceElement.addEventListener("change", function(evt)  {
    if (this.value === "C")
      codeSnippet.value = `#include <stdio.h>\n\nint main(void)  {\n\tprintf("hello world!");  // write code\n\treturn 0;\n}`;
    else if (this.value === "python") 
      codeSnippet.value = `print("hello world") # start coding!`;
    else if (this.value === "javascript") 
      codeSnippet.value = `console.log("hello world!")  // start coding!`;  
  })
})();

