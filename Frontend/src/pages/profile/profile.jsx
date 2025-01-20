
export const Profile = () => {
    return (
      <div style={{ backgroundColor: "#f9f4e7", minHeight: "100vh", padding: "20px", fontFamily: "Courier new" }}>
        <div style={{ textAlign: "center", marginBottom: "20px" }}>
          <div
            style={{
              width: "100px",
              height: "100px",
              backgroundColor: "#d3d3d3",
              borderRadius: "50%",
              margin: "0 auto",
            }}
          ></div>
          <h2 style={{ margin: "10px 0", fontWeight: "bold", color: "#000" }}>Username</h2>
          <p style={{ color: "#666", fontSize: "16px" }}>
            XX Siguiendo &nbsp;&nbsp; XX Seguidores
          </p>
          <p style={{ color: "#000", maxWidth: "600px", margin: "10px auto", fontSize: "14px" }}>
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
            industry's standard dummy text ever since the 1500s...
          </p>
        </div>
  
        <div
          style={{
            margin: "0 auto",
            maxWidth: "600px",
            border: "1px solid #ccc",
            borderRadius: "8px",
            overflowY: "scroll",
            height: "300px",
            backgroundColor: "#fff",
          }}
        >
          <div style={{ padding: "10px" }}>
            {["Galeria personal1", "Galeria personal2", "Galeria personal3", "Galeria personal4", "Galeria personal5", "Galeria personal6"].map((item, index) => (
              <div
                key={index}
                style={{
                  marginBottom: "10px",
                  padding: "15px",
                  backgroundColor: "#dcdcdc",
                  borderRadius: "5px",
                  textAlign: "center",
                  fontSize: "16px",
                  fontWeight: "bold",
                  color: "#000",
                }}
              >
                {item}
              </div>
            ))}
          </div>
        </div>
      </div>
    );
  };
  