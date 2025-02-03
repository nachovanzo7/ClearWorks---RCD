import { useState } from 'react';
import { Table } from 'evergreen-ui';
import { Link } from 'react-router-dom';


const profiles = [
    { id: 1, name: 'Pedro', lastActivity: '2022-12-01', ltv: 50 },
    { id: 2, name: 'Juan', lastActivity: '2022-11-25', ltv: 80 },
    { id: 3, name: 'Maria', lastActivity: '2022-11-10', ltv: 30 },
    { id: 4, name: 'Luis', lastActivity: '2022-10-25', ltv: 75 },
    { id: 5, name: 'Sofia', lastActivity: '2022-10-10', ltv: 60 },
];

const Tables = () => {
  const [filter, setFilter] = useState('');

  const nombreFiltrado = profiles.filter((profile) =>
    profile.name.toLowerCase().includes(filter.toLowerCase())
  );

  return (
    <Table>
      <Table.Head>
        <Table.SearchHeaderCell 
          onChange={(value) => setFilter(value)} 
          placeholder='Filtrar por nombre...'
        />
        <Table.TextHeaderCell>Fecha de ingreso</Table.TextHeaderCell>
        <Table.TextHeaderCell>Cantidad de obras</Table.TextHeaderCell>
      </Table.Head>
      <Table.Body height={240}>
        {nombreFiltrado.map((profile) => (
          <Table.Row key={profile.id} isSelectable onSelect={() => alert(profile.name)}>
            <Table.TextCell>
            <Link to={`/cliente/${profile.id}`} style={{ textDecoration: 'none', color: 'blue' }}>
                {profile.name}
              </Link>
              {profile.name}</Table.TextCell>
            <Table.TextCell>{profile.lastActivity}</Table.TextCell>
            <Table.TextCell isNumber>{profile.ltv}</Table.TextCell>
          </Table.Row>
        ))}
      </Table.Body>
    </Table>
  );
};

export default Tables;
