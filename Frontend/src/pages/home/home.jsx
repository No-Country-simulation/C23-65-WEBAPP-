import { useState } from "react";
import { useNavigate } from "react-router";

export const Home = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (email && password.length >= 8) {
      console.log("Login data:", { email, password });
      navigate("/hall");
    } else {
      setError("Por favor ingrese datos válidos.");
    }
  };

  return (
    <div className="min-h-screen bg-[#F0EAD6] flex flex-col items-center justify-center w-full h-full">
      <h1 className="text-4xl font-bold text-[#173044] mb-8">
        Museo Virtual
      </h1>
      <div className="w-[360px] h-[500px] bg-[#013220] p-6 rounded shadow-lg flex flex-col justify-center">
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="flex space-x-4">
            <div className="flex-1">
              <label
                htmlFor="email"
                className="block text-[#F1E4EB] text-sm font-medium mb-1"
              >
                Email
              </label>
              <input
                id="email"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full px-3 py-2 border border-[#F1E4EB] rounded bg-[#F1E4EB] text-[#013220] focus:outline-none focus:ring focus:ring-[#2CB67D]"
                required
              />
            </div>
            <div className="flex-1">
              <label
                htmlFor="password"
                className="block text-[#F1E4EB] text-sm font-medium mb-1"
              >
                Contraseña
              </label>
              <input
                id="password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full px-3 py-2 border border-[#F1E4EB] rounded bg-[#F1E4EB] text-[#013220] focus:outline-none focus:ring focus:ring-[#2CB67D]"
                required
              />
            </div>
          </div>
          {error && <p className="text-red-500 text-sm text-center">{error}</p>}
          <div className="flex justify-center">
            <button
              type="submit"
              className="px-6 py-2 bg-[#B87333] text-[#F1E4EB] font-bold rounded hover:bg-[#A65E2E] focus:outline-none focus:ring focus:ring-[#B87333]"
            >
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};


