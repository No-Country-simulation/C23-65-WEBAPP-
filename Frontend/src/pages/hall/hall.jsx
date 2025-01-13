import { useNavigate } from "react-router";

export const Hall = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-[#F0EAD6] flex flex-col">
      {/* Navbar */}
      <div className="w-full bg-[#013220] py-4 px-6 flex justify-between items-center">
        <div>
          <h1 className="text-xl font-bold text-[#F1E4EB]">Museo Virtual</h1>
        </div>
        <button
          className="w-10 h-10 bg-[#B87333] rounded-full focus:outline-none focus:ring focus:ring-[#A65E2E]"
          onClick={() => navigate("/profile")}
        ></button>
      </div>

      {/* Content */}
      <div className="flex-1 flex flex-col items-center justify-center space-y-8">
        <h2 className="text-3xl font-bold text-[#173044]">Bienvenido</h2>

        {/* Search Bar */}
        <div className="flex items-center space-x-2 bg-[#F1E4EB] px-4 py-2 rounded shadow-lg mb-8">
          <input
            type="text"
            placeholder="Buscar..."
            className="bg-[#F1E4EB] text-[#173044] placeholder-[#94A1B2] focus:outline-none"
          />
          <button className="text-[#013220] focus:outline-none">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              />
            </svg>
          </button>
        </div>

        {/* Buttons */}
        <div className="grid grid-cols-3 gap-6 max-w-3xl">
          {/* Left Column */}
          <div className="flex flex-col items-center space-y-6">
            <button
              className="bg-[#013220] text-[#F1E4EB] py-4 px-6 rounded shadow hover:bg-[#011E1A]"
              onClick={() => navigate("/int-galleries")}
            >
              Galerias internacionales
            </button>
            <button
              className="bg-[#013220] text-[#F1E4EB] py-4 px-6 rounded shadow hover:bg-[#011E1A]"
              onClick={() => navigate("/int-archaeo")}
            >
              Arqueologia Internacional
            </button>
          </div>

          {/* Middle Column */}
          <div className="flex items-center justify-center">
            <button
              className="bg-[#013220] text-[#F1E4EB] py-4 px-6 rounded shadow hover:bg-[#011E1A]"
              onClick={() => navigate("/my-space")}
            >
              Mi Espacio
            </button>
          </div>

          {/* Right Column */}
          <div className="flex flex-col items-center space-y-6">
            <button
              className="bg-[#013220] text-[#F1E4EB] py-4 px-6 rounded shadow hover:bg-[#011E1A]"
              onClick={() => navigate("/national-gallery")}
            >
              Galeria Nacional
            </button>
            <button
              className="bg-[#013220] text-[#F1E4EB] py-4 px-6 rounded shadow hover:bg-[#011E1A]"
              onClick={() => navigate("/national-archaeo")}
            >
              Arqueologia Nacional
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};