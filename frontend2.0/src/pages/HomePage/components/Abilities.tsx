//@ts-ignore
import styles from "../index.module.css"
import React from "react"
import { Typography, List, ListItem, ListItemAvatar, Avatar, ListItemText } from "@mui/material"

export default function Abilities() {
  return (
    <React.Fragment>
      <Typography className={styles.section_title} fontSize="25px" marginBottom="50px">
        Почему Swapper?
      </Typography>
      <List
        component="nav"
        sx={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <ListItem sx={{ maxWidth: "900px", marginBottom: "70px", marginRight: 30 }}>
          <ListItemAvatar
            sx={{
              marginRight: "20px",
            }}
          >
            <Avatar
              src="https://www.distilnfo.com/itadvisory/files/2019/12/Cloud-Computing.jpg"
              sx={{
                width: 170,
                height: 170,
              }}
            />
          </ListItemAvatar>
          <ListItemText
            primary="Удобство и Безопасность!"
            primaryTypographyProps={{
              fontSize: 25,
              fontWeight: "bold",
              marginBottom: "7px",
            }}
            secondary={
              <React.Fragment>
                <Typography fontSize={20} variant="body2" color="textPrimary">
                  Swapper предоставляет удобную и безопасную площадку для поиска и предоставления
                  услуг
                </Typography>
              </React.Fragment>
            }
          />
        </ListItem>
        <ListItem sx={{ maxWidth: "900px", marginBottom: "70px", marginLeft: 30 }}>
          <ListItemText
            primary="Легкость и Простота!"
            primaryTypographyProps={{
              fontSize: 25,
              fontWeight: "bold",
              marginBottom: "7px",
            }}
            secondary={
              <React.Fragment>
                <Typography fontSize={20} variant="body2" color="textPrimary">
                  Обширный, простой и интуитивно понятный функционал который поможет вам легко и
                  удобно совершать обмены
                </Typography>
              </React.Fragment>
            }
          />
          <ListItemAvatar
            sx={{
              marginRight: "50px",
            }}
          >
            <Avatar
              src="https://www.finskay.ru/storage/images/56c933d5c5f55e48d7f93f14b049953c.jpg"
              sx={{
                width: 170,
                height: 170,
              }}
            />
          </ListItemAvatar>
        </ListItem>
        <ListItem sx={{ maxWidth: "900px", marginBottom: "70px", marginRight: 30 }}>
          <ListItemAvatar
            sx={{
              marginRight: "20px",
            }}
          >
            <Avatar
              src="https://static.tildacdn.com/tild6339-6133-4537-b435-373632663039/solutions.png"
              sx={{
                width: 170,
                height: 170,
              }}
            />
          </ListItemAvatar>
          <ListItemText
            primary="Отзывчивая Техподдержка!"
            primaryTypographyProps={{
              fontSize: 25,
              fontWeight: "bold",
              marginBottom: "7px",
            }}
            secondary={
              <React.Fragment>
                <Typography fontSize={20} variant="body2" color="textPrimary">
                  Круглосуточная техподдержка, готовая помочь вам с любым вопросом в любое время
                </Typography>
              </React.Fragment>
            }
          />
        </ListItem>
      </List>
    </React.Fragment>
  )
}
