import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (email && password.length >= 8) {
      console.log('Login data:', { email, password });
      navigate('/hall');
    } else {
      setError('Por favor ingrese datos válidos.');
    }
  };

  return (
    <div className="min-h-screen bg-[#FDF6E3] flex items-center justify-center">
      <div className="w-80 bg-[#002B36] p-6 rounded shadow-lg">
        <h1 className="text-2xl font-bold text-[#FDF6E3] text-center mb-6">Museo Virtual</h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="email" className="block text-[#FDF6E3] text-sm font-medium mb-1">
              Email
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-3 py-2 border border-[#FDF6E3] rounded bg-[#FDF6E3] text-[#002B36] focus:outline-none focus:ring focus:ring-[#2CB67D]"
              required
            />
          </div>
          <div>
            <label htmlFor="password" className="block text-[#FDF6E3] text-sm font-medium mb-1">
              Contraseña
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-3 py-2 border border-[#FDF6E3] rounded bg-[#FDF6E3] text-[#002B36] focus:outline-none focus:ring focus:ring-[#2CB67D]"
              required
            />
          </div>
          {error && <p className="text-red-500 text-sm">{error}</p>}
          <button
            type="submit"
            className="w-full py-2 bg-[#A76F50] text-[#FDF6E3] font-bold rounded hover:bg-[#8C583C] focus:outline-none focus:ring focus:ring-[#A76F50]"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
