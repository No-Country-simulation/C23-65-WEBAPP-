import Slider from "react-slick";
import { GrNext, GrPrevious } from "react-icons/gr";
import PropTypes from "prop-types";

export const Carousel = ({ elements, color, gallery, isModalOpen }) => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    nextArrow: <GrNext color={`${gallery ? "black" : "white"}`} />,
    prevArrow: <GrPrevious color={`${gallery ? "black" : "white"}`} />,
  };

  return (
    <div
      className={`pb-10 w-4/5 flex justify-center ${
        color ? `bg-[#013220] rounded-2xl` : ""
      } ${gallery ? `border border-black rounded-2xl py-10` : ""} ${
        isModalOpen ? "pointer-events-none" : ""
      }`}
    >
      <Slider {...settings} className="w-5/6">
        {(elements || []).map((element, index) => (
          <div key={index}>{element}</div>
        ))}
      </Slider>
    </div>
  );
};

Carousel.propTypes = {
  elements: PropTypes.array.isRequired,
  color: PropTypes.bool,
  gallery: PropTypes.bool,
  isModalOpen: PropTypes.bool,
};
