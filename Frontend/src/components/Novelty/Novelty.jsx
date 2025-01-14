import PropTypes from "prop-types";
import { useNavigate } from "react-router";

export const Novelty = ({ id, title, imageURL, description }) => {
  const navigate = useNavigate();
  return (
    <div className="flex flex-col w-full">
      <h1 className=" text-xl font-semibold py-4 text-text-primary">{title}</h1>
      <div className="flex flex-row justify-around items-center w-full h-56">
        <div className="w-2/5 flex justify-center items-center">
          <img src={imageURL} alt={title} className="object-contain" />
        </div>
        <div className="w-2/5 h-full bg-[#D9D9D9] py-4 px-7 rounded-xl">
          <p className="overflow-hidden text-ellipsis line-clamp-6">
            {description}
          </p>
          <div className="flex justify-end">
            <button
              className="py-1 px-4 mt-2 bg-btn-delete text-white"
              onClick={() => navigate(`/galeria/${id}`)}
            >
              Ver más...
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

Novelty.propTypes = {
  id: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  imageURL: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
};
