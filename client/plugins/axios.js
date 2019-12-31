import axios from 'axios'

const service = axios.create({
  baseURL: process.env.HOST_URL + '/api',
  timeout: 5000
})

// service.interceptors.request.use(
//   config => {
//     return config
//   },
//   error => {
//     console.log(error)
//     return Promise.reject(error)
//   }
// )

// service.interceptors.response.use(
//   null,
//   error => {
//     console.log('err' + error)
//     return Promise.reject(error)
//   }
// )

export default service 