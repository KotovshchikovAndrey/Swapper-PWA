import React from "react"
import { Link } from "react-router-dom"
import { AppBar, Toolbar, Typography, Stack, Button } from "@mui/material"

export default function Navbar() {
  return (
    <AppBar sx={{ backgroundColor: "rgb(89, 242, 191)", boxShadow: "none", padding: 0.5 }}>
      <Toolbar sx={{ justifyContent: "space-between", alignItems: "center" }}>
        <Typography
          fontSize={30}
          variant="h6"
          color="inherit"
          component="div"
          sx={{
            cursor: "pointer",
          }}
        >
          <Link
            to="/"
            style={{
              textDecoration: "none",
              color: "inherit",
            }}
          >
            Swapper
          </Link>
        </Typography>
        <Stack direction="row" spacing={5}>
          <Button size="small" color={"info"} sx={{ color: "white" }}>
            Найти Сваппера
          </Button>
          <Button size="small" color={"info"} sx={{ color: "white" }}>
            Рейтинг Свапперов
          </Button>
          <Button size="small" color={"info"} sx={{ color: "white" }}>
            Сваппы Дня
          </Button>
        </Stack>
        <Button size="small" color={"info"} sx={{ color: "white" }}>
          <Link
            to="/auth"
            style={{
              textDecoration: "none",
              color: "inherit",
            }}
          >
            Регистрация / Авторизация
          </Link>
        </Button>
      </Toolbar>
    </AppBar>
  )
}
