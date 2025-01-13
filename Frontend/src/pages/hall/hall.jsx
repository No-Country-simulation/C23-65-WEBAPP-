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
      <div className="flex-1 flex flex-col items-center justify-center space-y-6">
        <h2 className="text-3xl font-bold text-[#173044]">Bienvenido</h2>
        <div className="w-full max-w-3xl grid grid-cols-3 gap-4">
          <button
            className="bg-[#013220] text-[#F1E4EB] py-4 px-6 rounded shadow hover:bg-[#011E1A]"
            onClick={() => navigate("/int-galleries")}
          >
            Galerias internacionales
          </button>
          <button
            className="bg-[#013220] text-[#F1E4EB] py-4 px-6 rounded shadow hover:bg-[#011E1A]"
            onClick={() => navigate("/national-gallery")}
          >
            Galeria Nacional
          </button>
          <button
            className="bg-[#013220] text-[#F1E4EB] py-4 px-6 rounded shadow hover:bg-[#011E1A]"
            onClick={() => navigate("/my-space")}
          >
            Mi Espacio
          </button>
          <button
            className="bg-[#013220] text-[#F1E4EB] py-4 px-6 rounded shadow hover:bg-[#011E1A]"
            onClick={() => navigate("/int-archaeo")}
          >
            Arqueologia Internacional
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
  );
};