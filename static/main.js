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
})