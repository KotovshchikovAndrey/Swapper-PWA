import React from "react"
import Navbar from "components/ui/navigation/Navbar"
import { Box, Typography } from "@mui/material"

export default function Header() {
  return (
    <React.Fragment>
      <Navbar />
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        sx={{
          backgroundSize: "contain",
          backgroundPosition: "center",
          height: "100vh",
          backgroundImage: "url(http://localhost/images/partnership.png)",
          backgroundRepeat: "no-repeat",
        }}
      >
        <Typography
          fontSize={20}
          align="center"
          maxWidth={700}
          lineHeight={1.7}
          padding={2.5}
          marginBottom={25}
          sx={{ backgroundColor: "rgba(255, 253, 242, 0.523)" }}
        >
          <Typography fontSize={25} fontWeight="bold" marginBottom={2.5}>
            Что такое Swapper?
          </Typography>
          Swapper - это сервис для поиска и осуществления взаимовыгодных отношений между людьми. Мы
          предоставляем удобную площадку для обмена, поиска и предоставления улуг
        </Typography>
      </Box>
    </React.Fragment>
  )
}
