//@ts-ignore
import email from "assets/email.png"
import React from "react"
import { Stack, Box, Typography, Button } from "@mui/material"

export default function Notification() {
  return (
    <React.Fragment>
      <Stack
        flexDirection="row"
        alignItems="center"
        justifyContent="center"
        padding="100px"
        paddingBottom="0"
        sx={{
          backgroundColor: "#1E90FF",
        }}
      >
        <Box component="img" src={email} maxWidth="330px" marginRight="170px" />
        <Stack maxWidth="500px">
          <Typography fontSize={25} color="#fff" fontWeight="bold" marginBottom="25px">
            Хотите получать оповещения?
          </Typography>
          <Typography fontSize={21} color="#fff" lineHeight="1.8" marginBottom="25px">
            Не пропусти повления новых и выгодных сваппов, подобранных специально для тебя. Будь в
            курсе событий!
          </Typography>
          <Button
            variant="contained"
            size="medium"
            sx={{
              color: "#fff",
              backgroundColor: "#4B0082",
              padding: "8px 25px",
              maxWidth: "130px",
              textTransform: "inherit",
              ":hover": {
                backgroundColor: "#8A2BE2",
              },
            }}
          >
            Хочу!
          </Button>
        </Stack>
      </Stack>
    </React.Fragment>
  )
}
