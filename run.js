const { spawn } = require('child_process');
//const childPython = spawn ('python', ['--version']);
const childPython = spawn ('python', ['../app.py']);
// const child Python = spawn ('python', ['codespace.py', 'OyeKool']);
childPython.stdout.on('data', (data) => {
console.log(`stdout: ${data}`);
});
childPython.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});
childPython.on('close', (code) =>{
  console.log(`child process exited with code ${code}`);
});
/*/
const inputs = document.querySelectorAll('[data-status]')

inputs.forEach(input =>{
  input.addEventListener('click', (e)=>{
    const status = input.dataset.status === 'unchecked' ? true : false
    if(status){
      inputs.forEach(input =>{
        input.dataset.status = 'unchecked'
      })
      input.dataset.status = 'checked'
    }else{
      input.dataset.status = 'unchecked'
    }
  })
})*/