export default function Login() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-md w-96">
        <h1 className="text-2xl font-bold mb-6">Login</h1>
        <form>
          <input type="email" placeholder="Email" className="w-full p-2 border rounded mb-4" />
          <input type="password" placeholder="Senha" className="w-full p-2 border rounded mb-4" />
          <button className="w-full bg-primary-600 text-white p-2 rounded hover:bg-primary-700">
            Entrar
          </button>
        </form>
      </div>
    </div>
  )
}
