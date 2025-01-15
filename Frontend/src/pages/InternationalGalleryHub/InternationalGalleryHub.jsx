import { Accordion } from "../../components/Accordion/Accordion";
import { Carousel } from "../../components/Carousel/Carousel";
import { Novelty } from "../../components/Novelty/Novelty";

export const InternationalGalleryHub = () => {
  const dataExample = [
    {
      id: "1",
      title: "galeria1",
      description:
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheet",
      imageURL:
        "https://images.adsttc.com/media/images/6267/37bd/79f7/2c01/6609/1000/newsletter/11g-7338.jpg?1650931661",
    },
    {
      id: "2",
      title: "galeria1",
      description:
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheet",
      imageURL:
        "https://images.adsttc.com/media/images/6267/37bd/79f7/2c01/6609/1000/newsletter/11g-7338.jpg?1650931661",
    },
    {
      id: "3",
      title: "galeria1",
      description:
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheet",
      imageURL:
        "https://images.adsttc.com/media/images/6267/37bd/79f7/2c01/6609/1000/newsletter/11g-7338.jpg?1650931661",
    },
    {
      id: "4",
      title: "galeria1",
      description:
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheet",
      imageURL:
        "https://images.adsttc.com/media/images/6267/37bd/79f7/2c01/6609/1000/newsletter/11g-7338.jpg?1650931661",
    },
    {
      id: "5",
      title: "galeria1",
      description:
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheet",
      imageURL:
        "https://images.adsttc.com/media/images/6267/37bd/79f7/2c01/6609/1000/newsletter/11g-7338.jpg?1650931661",
    },
  ];

  const elementsExample = dataExample.map(
    ({ id, description, imageURL, title }) => (
      <Novelty
        key={id}
        id={id}
        description={description}
        imageURL={imageURL}
        title={title}
      />
    )
  );
  const sections = [
    {
      title: "Section 1",
      links: [
        { tag: "Link 1", href: "#" },
        { tag: "Link 2", href: "#" },
        { tag: "Link 3", href: "#" },
      ],
    },

    {
      title: "Section 2",
      links: [
        { tag: "Link 4", href: "#" },
        { tag: "Link 5", href: "#" },
        { tag: "Link 6", href: "#" },
      ],
    },

    {
      title: "Section 3",
      links: [
        { tag: "Link 7", href: "#" },
        { tag: "Link 8", href: "#" },
        { tag: "Link 9", href: "#" },
      ],
    },
  ];

  return (
    <div className="flex flex-col h-screen items-center bg-background-page p-10">
      <h1 className="text-text-secondary font-semibold text-2xl">
        Galerías Internacionales
      </h1>
      <div className="flex flex-col items-start w-2/3 my-6">
        <h2 className="text-text-secondary font-semibold text-xl mb-7">
          Novedades
        </h2>
        <div className="w-full flex justify-center">
          <Carousel elements={elementsExample} color={true} />
        </div>
      </div>
      <div className="flex flex-col items-start w-2/3 my-6">
        <h2 className="text-text-secondary font-semibold text-xl">Galerías</h2>
        <Accordion section={sections} />
      </div>
    </div>
  );
};
